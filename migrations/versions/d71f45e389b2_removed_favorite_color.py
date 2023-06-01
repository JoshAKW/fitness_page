"""removed favorite color

Revision ID: d71f45e389b2
Revises: 6ed5235ce5fb
Create Date: 2023-05-31 12:01:56.937465

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd71f45e389b2'
down_revision = '6ed5235ce5fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workouts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=True),
    sa.Column('date_posted', sa.DateTime(), nullable=True),
    sa.Column('slug', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer1_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer1_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise10',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer10_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer10_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise11',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer11_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer11_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise12',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer12_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer12_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer2_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer2_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise3',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer3_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer3_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise4',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer4_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer4_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise5',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer5_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer5_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise6',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer6_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer6_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise7',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer7_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer7_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise8',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer8_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer8_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exercise9',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('set1', sa.String(length=50), nullable=True),
    sa.Column('set2', sa.String(length=50), nullable=True),
    sa.Column('set3', sa.String(length=50), nullable=True),
    sa.Column('set4', sa.String(length=50), nullable=True),
    sa.Column('set5', sa.String(length=50), nullable=True),
    sa.Column('set6', sa.String(length=50), nullable=True),
    sa.Column('excer9_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['excer9_id'], ['workouts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('favorite_color')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favorite_color', mysql.VARCHAR(length=120), nullable=True))

    op.drop_table('exercise9')
    op.drop_table('exercise8')
    op.drop_table('exercise7')
    op.drop_table('exercise6')
    op.drop_table('exercise5')
    op.drop_table('exercise4')
    op.drop_table('exercise3')
    op.drop_table('exercise2')
    op.drop_table('exercise12')
    op.drop_table('exercise11')
    op.drop_table('exercise10')
    op.drop_table('exercise1')
    op.drop_table('workouts')
    # ### end Alembic commands ###